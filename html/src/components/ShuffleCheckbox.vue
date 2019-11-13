<template>
  <label class="checkbox">
    <input type="checkbox" v-model="checked" />
    Shuffle {{checked ? 'On.':'Off.'}}
  </label>
</template>


<script>
import { mapState, mapActions } from "vuex"

export default {
  methods: {
    ...mapActions(["toggleShuffleMode"])
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