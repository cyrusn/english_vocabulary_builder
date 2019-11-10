<template>
  <div class="col-auto">
    <div class="input-group p-2">
      <div class="input-group-prepend">
        <span class="input-group-text">Page No.</span>
      </div>
      <input
        type="number"
        min="1"
        :max="totalPage"
        aria-label="Page No."
        class="form-control"
        v-model.number.lazy="localPageNo"
        :class="invalid"
      />
      <div class="input-group-append">
        <span class="input-group-text">&nbsp;of {{totalPages}}</span>
      </div>
      <div class="invalid-feedback">Must be an positve interger less than total pages</div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex"

export default {
  data() {
    return {
      invalid: {
        "is-invalid": false
      }
    }
  },
  computed: {
    ...mapState(["pageNo"]),
    ...mapGetters(["totalPages"]),
    localPageNo: {
      get() {
        return this.pageNo
      },
      set(n) {
        const { totalPages, invalid, updatePageNo } = this
        if (typeof n !== "number" || n < -1 || n > totalPages) {
          invalid["is-invalid"] = true
          return
        }
        invalid["is-invalid"] = false
        updatePageNo(n)
      }
    }
  },
  methods: {
    ...mapActions(["updatePageNo"])
  }
}
</script>