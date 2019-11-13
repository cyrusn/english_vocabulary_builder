<template>
  <div class="field has-addons">
    <p class="control" v-show="!isShuffleMode">
      <span class="button is-static">Page</span>
    </p>
    <p class="control" v-show="!isShuffleMode">
      <input
        type="number"
        min="1"
        :max="totalPages"
        aria-label="Page No."
        class="input"
        placeholder="Page No"
        v-model.number="localPageNo"
      />
    </p>
    <p class="control" v-show="!isShuffleMode">
      <span class="button is-static">/ {{totalPages}}</span>
    </p>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex"

export default {
  computed: {
    ...mapState(["pageNo", "isShuffleMode"]),
    ...mapGetters(["totalPages"]),
    localPageNo: {
      get() {
        return this.pageNo
      },
      set(n) {
        const { totalPages, updatePageNo } = this
        if (typeof n !== "number" || n < -1 || n > totalPages) {
          return
        }
        updatePageNo(n)
      }
    }
  },
  methods: {
    ...mapActions(["updatePageNo"])
  }
}
</script>