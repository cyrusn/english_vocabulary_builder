<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light">
    <div class="col-auto">
      <div class="form-check">
        <input class="form-check-input" type="checkbox" v-model="checked" />
        <label class="form-check-label">Shuffle {{checked ? 'On.':'Off.'}}</label>
      </div>
    </div>
    <div class="col-auto" v-show="isShuffleMode">
      <button @click="updateWords" class="btn btn-primary">Shuffle</button>
    </div>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbar"
      aria-expanded="false"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbar">
      <form class="form-row align-items-center">
        <library-selector></library-selector>
        <page-input v-show="!isShuffleMode"></page-input>
      </form>
    </div>
  </nav>
</template>

<script>
import LibrarySelector from "@/components/LibrarySelector.vue"
import PageInput from "@/components/PageInput.vue"
import { mapState, mapActions } from "vuex"

export default {
  components: {
    LibrarySelector,
    PageInput
  },
  methods: {
    ...mapActions(["toggleShuffleMode", "updateWords"])
  },
  computed: {
    ...mapState(["isShuffleMode"]),
    checked: {
      get() {
        return this.isShuffleMode
      },
      set() {
        this.toggleShuffleMode()
      }
    }
  }
}
</script>