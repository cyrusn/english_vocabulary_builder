<template>
  <div class="card p-3 my-2">
    <word-title :ipa="word.ipa" :title="word.title" :id="word.id"></word-title>
    <div v-for="(session, s) in word.sessions" :key="s">
      <div v-for="(definition, k) in session[1].slice(0,3)" :key="k">
        <div class="row border-bottom">
          <div class="col-md-6">
            <span class="badge badge-pill badge-danger">{{session[0]}}</span>
            <span class="font-weight-light font-italic text-primary">&nbsp;{{definition[0]}}</span>
          </div>
          <div class="col-md-6">
            <div class v-for="(example, n) in definition[1]" :key="n">
              <example :chi="example[1]" :eng="example[0]"></example>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import WordTitle from "@/components/WordTitle.vue"
import Example from "@/components/Example.vue"

export default {
  props: ["word"],
  components: {
    Example,
    WordTitle
  }
}
</script>