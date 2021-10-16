<template>
  <button
    class="button"
    ref="btn"
    v-on:click.passive="buttonClick"
    :disabled="isDisabled"
    @click="callPython"
  >
    <img src="@/assets/pepega.png" class="button-img" />
    {{ buttonText }}

    {{ ready }}
  </button>
  {{ resp }}
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";

declare global {
  interface Window {
    pywebview: any;
  }
}
@Options({
  props: {
    buttonText: String,
  },
})
export default class BigButton extends Vue {
  isDisabled = false;
  buttonText!: string;
  ready = "not ready";
  resp = "";

  // Create the ripple effect on the button by using the button event
  createRipple(event: MouseEvent): void {
    var button: any = this.$refs.btn;
    const circle = document.createElement("span");
    const diameter = Math.max(button.clientWidth, button.clientHeight);
    const radius = diameter / 2;
    circle.style.width = circle.style.height = `${diameter}px`;
    circle.style.left = `${event.clientX - (button.offsetLeft + radius)}px`;
    circle.style.top = `${event.clientY - (button.offsetTop + radius)}px`;
    circle.classList.add("ripple");
    const ripple = button.getElementsByClassName("ripple")[0];

    if (ripple) {
      ripple.remove();
    }
    button.appendChild(circle);
  }

  // This function is here to disable double clicks on this button
  disableButton(): void {
    this.isDisabled = true;
    setTimeout(() => {
      this.isDisabled = false;
    }, 2000);
  }

  // Wrapper that does the passive button click stuff
  buttonClick(event: MouseEvent): void {
    this.createRipple(event);
    this.disableButton();
  }

  callPython(): void {
    var resp: Promise<string> = window.pywebview.api.do_something()
    
    resp.then((res) => {
      this.resp = res;
    });
  }

  setReady(): void {
    this.ready = "ready";
  }
  mounted() {
    window.addEventListener("pywebviewready", this.setReady);
  }
}
</script>
<style lang="scss">
$buttoncolor: #1452ff;

.button {
  height: 200px;
  width: 200px;
  background-color: $buttoncolor;
  position: relative;
  overflow: hidden;
  transition: background 400ms;
  color: #fff;
  padding: 1rem 2rem;
  font-family: "Roboto", sans-serif;
  font-size: 1.5rem;
  outline: 0;
  border: 0;
  border-radius: 0.25rem;
  box-shadow: 0 0 0.5rem rgba(0, 0, 0, 0.3);
  cursor: pointer;
}

span.ripple {
  position: absolute; /* The absolute position we mentioned earlier */
  border-radius: 50%;
  transform: scale(0);
  animation: ripple 600ms linear;
  background-color: rgba(255, 255, 255, 0.7);
}

@keyframes ripple {
  to {
    transform: scale(4);
    opacity: 0;
  }
}

.button-img {
  height: 100px;
  width: 160px;
}
</style>