<template>
  <ul class="pagination pagination-sm justify-content-center">
    <li class="page-item" @click="previous">
      <a href="#" class="page-link">&laquo;</a>
    </li>
    <li class="page-item" v-show="pageNo > 3 " @click="updatePageNo(1)">
      <a href="#" class="page-link">1</a>
    </li>
    <li class="page-item disabled" v-show="pageNo > 4">
      <a href="#" class="page-link">...</a>
    </li>
    <li
      class="page-item"
      :class="{active: pageNo == i}"
      v-for="i in range"
      @click="updatePageNo(i)"
      :key="i"
    >
      <a href="#" class="page-link">{{i}}</a>
    </li>
    <li class="page-item disabled" v-show="pageNo < (totalPages - 3)">
      <a href="#" class="page-link">...</a>
    </li>
    <li class="page-item" v-show="pageNo < (totalPages - 2)" @click="updatePageNo(totalPages)">
      <a href="#" class="page-link">{{totalPages}}</a>
    </li>
    <li class="page-item" @click="next">
      <a href="#" class="page-link">&raquo;</a>
    </li>
  </ul>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex"
export default {
  data() {
    return {
      active: false,
      width: 5
    }
  },
  computed: {
    ...mapState(["pageNo", "wordsPerPage", "libraryWordsLength"]),
    ...mapGetters(["totalPages"]),
    median() {
      const { width } = this
      return Math.floor((width + 1) / 2)
    },
    range() {
      const list = []
      const { width, pageNo, median, totalPages } = this

      let startingIndex = pageNo - median + 1
      if (pageNo < median) {
        startingIndex = 1
      }

      if (startingIndex > totalPages - width) {
        startingIndex = totalPages - width + 1
      }

      while (list.length < width) {
        list.push(startingIndex)
        startingIndex++
      }
      return list
    }
  },
  methods: {
    ...mapActions(["updatePageNo"]),
    next() {
      const { pageNo, totalPages, updatePageNo } = this
      if (pageNo < totalPages) {
        updatePageNo(pageNo + 1)
      }
    },
    previous() {
      const { pageNo, updatePageNo } = this
      if (pageNo > 1) {
        updatePageNo(pageNo - 1)
      }
    }
  }
}
</script>