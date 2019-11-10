<template>
  <div class="container-fluid lead">
    <navbar></navbar>
    <pagination v-show="!isShuffleMode" class="mt-2"></pagination>
    <session v-for="word in words" :word="word" :key="word.id"></session>
    <pagination v-show="!isShuffleMode"></pagination>
  </div>
</template>

<script>
import Session from "@/components/Session.vue"
import Navbar from "@/components/Navbar.vue"
import Pagination from "@/components/Pagination.vue"

import { mapState, mapActions } from "vuex"

export default {
  name: "app",
  components: {
    Pagination,
    Navbar,
    Session
  },
  data() {
    return {}
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
