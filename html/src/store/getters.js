export default {
  totalPages: state => {
    const { librarySize, wordsPerPage } = state;
    return Math.floor(librarySize / wordsPerPage) + 1;
  }
};
