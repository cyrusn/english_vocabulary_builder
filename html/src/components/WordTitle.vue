<template>
  <div class="card-title">
    <h2>
      <span @click="toggle_show" class="badge badge-info">{{id}}</span>
      <span v-show="show" class>&nbsp;{{title}}</span>
      <small>
        <span class="font-weight-light text-danger">&nbsp;/{{ipa}}/</span>
      </small>
    </h2>
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