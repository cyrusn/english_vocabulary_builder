<template>
  <div>
    <div class="tags are-medium has-addons">
      <a class="tag is-dark" @click="toggle_show">{{id}}</a>
      <span class="tag is-light is-danger">/{{ipa}}/</span>
    </div>
    <h2 class="subtitle is-2 is-italic has-text-weight-semibold" v-show="show">{{title}}</h2>
  </div>
</template>

<script>
export default {
  props: ["title", "ipa", "id"],
  methods: {
    toggle_show() {
      this.show = !this.show
    }
  },
  data() {
    return {
      show: false
    }
  }
}
</script>