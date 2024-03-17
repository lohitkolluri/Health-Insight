<script lang="ts">
  import {
    TextInput,
    Button,
    Tile,
    Form,
    TextInputSkeleton,
  } from "carbon-components-svelte";
  import SendFilled from "carbon-icons-svelte/lib/SendFilled.svelte";
  import Stethoscope from "carbon-icons-svelte/lib/Stethoscope.svelte";
  import { DoctorSocket } from "../../types";
  import { onDestroy } from "svelte";

  let value = "";
  let x: {
    message?: string;
    type: "patient" | "bot";
  }[] = [
    {
      message:
        "Hello I'm Health Insight, your medical knowledge assistant ask me any questions about your prescription or your condition",
      type: "bot",
    },
  ];
  DoctorSocket.emit("patient_mode", true);

  DoctorSocket.on("patient_message", (content: { text: string; done: boolean }) => {
    if (x[x.length - 1].type === "bot") {
      x = [...x.slice(0, x.length - 1), { message: content.text, type: "bot" }];
    } else {
      x = [...x, { message: content.text, type: "bot" }];
    }
    if (content.done && value) {
      postMessage();
    }
  });

  DoctorSocket.on("patient_transcript", (text) => {
    value = text;
    postMessage();
  });

  const postMessage = () => {
    if (value.trim() !== "") {
      x = [...x, { message: value, type: "patient" }];
      DoctorSocket.emit("patient_message", value);
      value = "";
    }
  };

  onDestroy(() => {
    DoctorSocket.emit("patient_mode", false);
  });
</script>
<svelte:head>
  <title>Health Insight Patient</title> 
</svelte:head>
<div class="h-[93vh] flex flex-col bg-repeat bg-x relative">
  <div class="flex flex-col gap-y-3  mb-22 lg:w-[70%] mx-auto">
    {#each x as y}
      <div
        class="flex   {y.type === 'patient' ? 'flex-row-reverse' : 'flex-row'}"
      >
        {#if y.type !== "patient"}
          <div class="rounded-full pt-20px">
            <Stethoscope size={32} class="block m-auto " />
          </div>
        {/if}
        <Tile
          class="w-[60%] bg-gradient-to-r from-[#250358] to-[#440c66] rounded-md shadow-sm {y.type === 'patient'
            ? 'ml-auto'
            : 'mr-auto'}"
        >
          {#if y.message}
            <p>{y.message}</p>
          {/if}
        </Tile>
      </div>
    {/each}
  </div>

  <div class="flex absolute bottom-1 w-full px-6 py-3 bg-dark-600">
    <Form on:submit={postMessage} class=" w-full flex">
      <TextInput
        size="xl"
        hideLabel
        labelText="User name"
        placeholder="Ask your questions here"
        bind:value
        autofocus
      />
      <Button type="submit" kind="ghost" icon={SendFilled} size="xl" />
    </Form>
  </div>
</div>

<style>
  .bg-x {
    background-image: url("/bg.svg");
  }
</style>
