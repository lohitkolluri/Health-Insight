<script lang="ts">
  import "carbon-components-svelte/css/g80.css";
  import "virtual:uno.css";
  import Nav from "$lib/Nav.svelte";
  export const ssr = false;

</script>

<Nav />
<div class="mt-15" >
  <slot />
</div>
<style>
  :global(body) {
    background: radial-gradient(#27212e, #221530);
    color: #d9c9ee;
}</style>

