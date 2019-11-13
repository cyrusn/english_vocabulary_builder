export default {
  updateWords({ commit, state }) {
    const {
      allWords,
      pageNo,
      wordsPerPage,
      isShuffleMode,
      librarySize
    } = state;
    let words;
    if (isShuffleMode) {
      const items = [];
      while (items.length < wordsPerPage) {
        const n = Math.floor(Math.random() * librarySize);
        if (!items.includes(n)) {
          items.push(n);
        }
      }
      words = items.sort((a, b) => a - b).map(n => allWords[n]);
    } else {
      const range = [pageNo - 1, pageNo];
      words = [...allWords.slice(...range.map(x => x * wordsPerPage))];
    }
    commit("updateWords", words);
  },
  updatePageNo({ commit, dispatch }, n) {
    commit("updatePageNo", n);
    dispatch("updateWords");
  },
  toggleShuffleMode({ commit, dispatch }) {
    commit("toggleShuffleMode");
    dispatch("updateWords");
  },
  async fetchLibrary({ commit, state }) {
    const { library } = state;
    await fetch(`./data/${library}`)
      .then(response => response.json())
      .then(json => {
        commit("updateLibrarySize", json.length);
        commit("updateAllWords", json);
      });
  },
  async updateLibrary({ commit, dispatch }, library) {
    commit("updateLibrary", library);
    commit("updatePageNo", 1);
    await dispatch("fetchLibrary");
    dispatch("updateWords");
  }
};
