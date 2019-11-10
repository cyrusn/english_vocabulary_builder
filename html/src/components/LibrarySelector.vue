<template>
  <div class="col-auto">
    <div class="input-group p-2">
      <div class="input-group-prepend">
        <span class="input-group-text">Library</span>
      </div>
      <select class="custom-select" v-model="value" @change="onUpdate(value)">
        <option
          v-for="(option, key) in options"
          v-bind:value="option.value"
          :key="key"
        >{{ option.text }}</option>
      </select>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState } from "vuex"

export default {
  data() {
    return {
      options: [
        { text: "Basic", value: "basic.json" },
        { text: "Advance", value: "advance.json" },
        { text: "Master", value: "master.json" }
      ]
    }
  },
  computed: {
    ...mapState(["library"]),
    value: {
      get() {
        return this.library
      },
      set(library) {
        this.updateLibrary(library)
      }
    }
  },
  methods: {
    ...mapActions(["updateLibrary"]),
    ...mapMutations(["updateWords"]),
    onUpdate(value) {
      const { updateLibrary, updateWords } = this
      updateLibrary(value, updateWords)
    }
  }
}
</script>