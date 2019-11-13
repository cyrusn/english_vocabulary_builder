<template>
  <div class="level-item">
    <div class="field has-addons">
      <p class="control">
        <span class="button is-static">Library</span>
      </p>
      <div class="control">
        <div class="select">
          <select v-model="value" @change="onUpdate(value)">
            <option disabled value>Please select one</option>
            <option
              v-for="(option, key) in options"
              v-bind:value="option.value"
              :key="key"
            >{{ option.text }}</option>
          </select>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState, mapGetters } from "vuex"

export default {
  data() {
    return {
      value: "",
      options: [
        { text: "Basic", value: "basic.json" },
        { text: "Advance", value: "advance.json" },
        { text: "Master", value: "master.json" }
      ]
    }
  },
  computed: {
    ...mapState(["library", "isShuffleMode"]),
    ...mapGetters(["totalPages"])
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