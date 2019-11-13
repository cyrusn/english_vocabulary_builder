<template>
  <div class="box">
    <word-title :ipa="word.ipa" :title="word.title" :id="word.id" />
    <div v-for="(section, s) in word.sections" :key="s">
      <div v-for="(definition, k) in section[1].slice(0,3)" :key="k" class="panel is-info">
        <example-title :partOfSpeech="section[0]" :definition="definition[0]" />
        <example
          class
          v-for="(example, n) in definition[1]"
          :key="n"
          :chi="example[1]"
          :eng="example[0]"
        />
      </div>
    </div>
  </div>
</template>

<script>
import WordTitle from "@/components/WordTitle.vue"
import Example from "@/components/Example.vue"
import ExampleTitle from "@/components/ExampleTitle.vue"

export default {
  props: ["word"],
  components: {
    Example,
    ExampleTitle,
    WordTitle
  }
}
</script>