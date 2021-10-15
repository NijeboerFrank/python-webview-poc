<template>
  <div class="home">
    <BigButton buttonText="Start"></BigButton>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import BigButton from '@/components/BigButton.vue'

@Options({
  components: {
    BigButton
  },
})
export default class Home extends Vue {}
</script>
