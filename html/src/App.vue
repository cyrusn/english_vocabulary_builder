<template>
  <div>
    <setting />
    <pagination v-show="!isShuffleMode" />

    <div class="container">
      <word v-for="word in words " :word="word" :key="word.id" />
    </div>
    <pagination v-show="!isShuffleMode" />
  </div>
</template>

<script>
import Word from "@/components/Word.vue"
import Setting from "@/components/Setting.vue"
import Pagination from "@/components/Pagination.vue"

import { mapState, mapActions } from "vuex"

export default {
  name: "app",
  components: {
    Pagination,
    Setting,
    Word
  },
  computed: {
    ...mapState(["words", "library", "pageNo", "isShuffleMode"])
  },
  created() {
    const { updateLibrary, library } = this
    updateLibrary(library)
  },
  methods: {
    ...mapActions(["updateLibrary"])
  }
}
</script>
