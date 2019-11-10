import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    library: "basic.json",
    wordsPerPage: 10,
    pageNo: 1,
    libraryWordsLength: 0,
    words: [],
    isShuffleMode: true,
    allWords: []
  },
  getters: {
    totalPages: state => {
      const { libraryWordsLength, wordsPerPage } = state;
      return Math.floor(libraryWordsLength / wordsPerPage) + 1;
    }
  },
  mutations: {
    updateAllWords(state, words) {
      Vue.set(state, "allWords", [...words]);
    },
    updateWords(state, words) {
      Vue.set(state, "words", words);
    },
    updatePageNo(state, n) {
      state.pageNo = n;
    },
    updateLibraryWordsLength(state, n) {
      state.libraryWordsLength = n;
    },
    updateLibrary(state, library) {
      state.library = library;
    },
    updateWordsPerPage(state, n) {
      state.wordsPerPage = n;
    },
    toggleShuffleMode(state) {
      state.isShuffleMode = !state.isShuffleMode;
    }
  },
  actions: {
    updatePageNo({ commit, dispatch }, n) {
      commit("updatePageNo", n);
      dispatch("updateWords");
    },
    toggleShuffleMode({ commit, dispatch }) {
      commit("toggleShuffleMode");
      dispatch("updateWords");
    },
    updateWords({ commit, state }) {
      const {
        allWords,
        pageNo,
        wordsPerPage,
        isShuffleMode,
        libraryWordsLength
      } = state;
      if (isShuffleMode) {
        const items = [];
        while (items.length < wordsPerPage) {
          const n = Math.floor(Math.random() * libraryWordsLength);
          if (items.indexOf(n) == -1) {
            items.push(n);
          }
        }
        const words = items.sort((a, b) => a - b).map(n => allWords[n]);
        commit("updateWords", words);
      } else {
        const range = [pageNo - 1, pageNo];
        commit("updateWords", [
          ...allWords.slice(...range.map(x => x * wordsPerPage))
        ]);
      }
    },
    async fetchLibrary({ commit, state }) {
      const { library } = state;
      await fetch(`./data/${library}`)
        .then(response => response.json())
        .then(json => {
          commit("updateLibraryWordsLength", json.length);
          commit("updateAllWords", json);
        });
    },
    async updateLibrary({ commit, dispatch }, library) {
      commit("updateLibrary", library);
      await dispatch("fetchLibrary");
      dispatch("updateWords");
    }
  }
});
