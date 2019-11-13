<template>
  <div>
    <a class="panel-block" @click="toggle_show">
      <span class="tag is-light is-success">例</span>
      &nbsp;
      <span class="is-italic">{{chi}}</span>
    </a>
    <div v-show="show" class="panel-block">
      <span class="tag is-light is-warning">e.g.</span>
      &nbsp;
      <span class="is-italic">{{eng}}</span>
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