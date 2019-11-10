<template>
  <div>
    <div @click="toggle_show">
      <span class="badge badge-success">例</span>
      {{chi}}
    </div>
    <div v-show="show">
      <span class="badge badge-warning">e.g.</span>
      {{eng}}
    </div>
  </div>
</template>

<script>
export default {
  name: "example",
  props: ["chi", "eng"],
  data() {
    return {
      show: false
    }
  },
  methods: {
    toggle_show() {
      this.show = !this.show
    }
  }
}
</script>