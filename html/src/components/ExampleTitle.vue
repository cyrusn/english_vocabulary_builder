<template>
  <div class="panel-heading">
    <span class="tag is-light is-info">{{partOfSpeech}}</span>
    &nbsp;
    <span>{{definition}}</span>
  </div>
</template>

<script>
export default {
  props: ["partOfSpeech", "definition"]
}
</script>