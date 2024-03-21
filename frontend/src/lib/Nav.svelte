<script lang="ts">
  import { page } from "$app/stores";
  import { Button, Header, HeaderNav, HeaderNavItem } from "carbon-components-svelte";
  import { DoctorSocket, connected } from "../types";

  let isSideNavOpen = false;
  let running = false;

  const stopMic = () => {
    DoctorSocket.emit("stop_recording", undefined, (value: boolean) => {
      if (value) {
        running = false;
      }
    });
  };

  const startMic = () => {
    DoctorSocket.emit("start_recording", undefined, (value: boolean) => {
      if (value) {
        running = true;
      }
    });
  };
</script>

<Header bind:isSideNavOpen class="header">
  <a href="/" class="home-link">HEALTH INSIGHT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a> 
  {#if $connected}
    <Button on:click={running ? stopMic : startMic} class="mic-button">
      {#if running}
        <!-- Microphone active icon -->
        <img src="https://img.icons8.com/ios-filled/100/radio-studio.png" alt="Microphone Active" width="25" height="25">
      {:else}
        <!-- Microphone inactive icon -->
        <img src="https://img.icons8.com/ios-filled/100/block-microphone.png" alt="Microphone Inactive" width="22" height="22">
      {/if}
    </Button>
  {:else}
    <Button on:click={stopMic} disabled>Not connected</Button>
  {/if}
  
  <HeaderNav>
    <HeaderNavItem
      isSelected={$page.url.pathname === "/doctor" ? true : false}
      href="/doctor"
      text="Doctor companion"
    />
    <HeaderNavItem
      isSelected={$page.url.pathname === "/patient" ? true : false}
      href="/patient"
      text="Patient companion"
    />
  </HeaderNav>
</Header>

<style>
  .header {
    background-color: #0078D4; /* Set header background color */
    color: white; /* Set text color */
    padding: 1rem; /* Add padding */
    display: flex; /* Set display to flex */
    justify-content: space-between; /* Align items horizontally */
    align-items: center; /* Align items vertically */
  }

  .home-link {
    text-decoration: none; /* Remove underline from link */
    color: inherit; /* Inherit text color */
    font-weight: bold; /* Set font weight to bold */
    font-size: 1.2rem; /* Set font size */
  }

  .mic-button {
    background-color: transparent; 
    border: none; 
    cursor: pointer; 
    padding: calc(0.875rem - 3px) 10px calc(0.875rem - 3px) 10px; /* Added padding */
  }

  .mic-button:hover {
    filter: brightness(1.2); 
  }

  .mic-button:focus {
    outline: none; 
  }

  .mic-button img {
    vertical-align: middle; 
  }

  .mic-button:disabled {
    cursor: not-allowed; 
  }
</style>
