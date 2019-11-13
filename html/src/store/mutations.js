import Vue from "vue";
export default {
  updateAllWords(state, words) {
    Vue.set(state, "allWords", [...words]);
  },
  updateWords(state, words) {
    Vue.set(state, "words", words);
  },
  updatePageNo(state, n) {
    state.pageNo = n;
  },
  updateLibrarySize(state, n) {
    state.librarySize = n;
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
};
