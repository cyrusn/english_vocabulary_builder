<template>
  <div class="box">
    <div class="container">
      <nav class="pagination is-small" role="navigation">
        <ul class="pagination-list">
          <li>
            <a href="#" class="pagination-previous" @click="previous">&laquo;</a>
          </li>
          <li v-show="pageNo > 2 " @click="updatePageNo(1)">
            <a class="pagination-link" href="#">1</a>
          </li>
          <li v-show="pageNo > 3">
            <span class="pagination-ellipsis">&hellip;</span>
          </li>
          <li v-for="i in range" @click="updatePageNo(i)" :key="i">
            <a class="pagination-link" :class="{'is-current': pageNo == i}" href="#">{{i}}</a>
          </li>
          <li v-show="pageNo < (totalPages - 2)">
            <span class="pagination-ellipsis">&hellip;</span>
          </li>
          <li v-show="pageNo < (totalPages - 1)" @click="updatePageNo(totalPages)">
            <a class="pagination-link" href="#">{{totalPages}}</a>
          </li>
          <li>
            <a class="pagination-next" @click="next">&raquo;</a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex"
export default {
  data() {
    return {
      width: 3
    }
  },
  computed: {
    ...mapState(["pageNo", "wordsPerPage"]),
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