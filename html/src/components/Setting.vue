<template>
  <nav class="navbar is-fixed-top">
    <div class="container">
      <div class="navbar-brand">
        <div class="navbar-item">
          <shuffle-button v-if="isShuffleMode"></shuffle-button>
          <page-input v-else></page-input>
        </div>
        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="true"
          @click="isActive['is-active'] = !isActive['is-active']"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" :class="isActive">
        <div class="navbar-start">
          <div class="navbar-item">
            <library-selector></library-selector>
          </div>
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <shuffle-checkbox></shuffle-checkbox>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import LibrarySelector from "@/components/LibrarySelector.vue"
import PageInput from "@/components/PageInput.vue"
import ShuffleButton from "@/components/ShuffleButton.vue"
import ShuffleCheckbox from "@/components/ShuffleCheckbox.vue"
import { mapState } from "vuex"

export default {
  data() {
    return {
      isActive: {
        "is-active": false
      }
    }
  },
  components: {
    LibrarySelector,
    PageInput,
    ShuffleButton,
    ShuffleCheckbox
  },
  computed: {
    ...mapState(["isShuffleMode"])
  }
}
</script>