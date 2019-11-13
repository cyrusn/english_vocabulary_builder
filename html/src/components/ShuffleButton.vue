<template>
  <a @click="updateWords" role="button" class="button is-primary">Shuffle</a>
</template>

<script>
import { mapActions } from "vuex"

export default {
  methods: {
    ...mapActions(["updateWords"])
  }
}
</script>