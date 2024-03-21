<script lang="ts">
  import { Tile, Content } from "carbon-components-svelte";
  import SvelteMarkdown from "svelte-markdown";
  import { DoctorSocket, type TranscriptMessage } from "../types";
  import { onMount } from "svelte";

  let live: string;

  onMount(async () => {
    DoctorSocket.on("transcript", (x) => {
      console.log(x);
      live = x.replaceAll("\n", "\n\n");
    });
  });
</script>

<div class="conversation-container">
  <Tile class="conversation-header">
    <p class="conversation-title">Your conversation</p>
  </Tile>

  <Content class="conversation-content">
    {#if live}
      <SvelteMarkdown source={live} />
    {:else}
      <p class="text-gray-500">Conversation transcripts go here</p>
    {/if}
  </Content>
</div>

<style>
  .conversation-container {
    border: 2px solid #250358;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    height: 100%;
    position: relative; /* Add relative positioning to the container */
  }

  .conversation-header {
    padding: 10px;
    background-color: #250358;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .conversation-title {
    font-size: 1.2rem;
    font-weight: bold;
  }

  .conversation-content {
    flex: 1;
    padding: 10px;
    overflow-y: auto;
    position: relative; /* Add relative positioning to the content */
  }
</style>
