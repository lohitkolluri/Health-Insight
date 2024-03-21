<script lang="ts">
  import { Tile, TextArea, Button, ButtonSet } from "carbon-components-svelte";
  import ArrowRight from "carbon-icons-svelte/lib/ArrowRight.svelte";
  import DiagramReference from "carbon-icons-svelte/lib/DiagramReference.svelte";
  import { onMount } from "svelte";
  import { DoctorSocket } from "../types";

  let value = ``;

  onMount(() => {
    DoctorSocket.on("generate_notes", (x) => {
      console.log(x);
      value = x;
    });
  });

  const generate = () => {
    DoctorSocket.emit("generate_notes", value);
  };

  const setSummary = () => {
    // Create a Blob with the summary content
    const blob = new Blob([value], { type: 'text/plain' });

    // Create a temporary anchor element
    const a = document.createElement('a');
    a.style.display = 'none';

    // Set the href attribute to a URL created from the Blob
    a.href = window.URL.createObjectURL(blob);

    // Set the download attribute to specify the file name
    a.download = 'consultation_summary.txt';

    // Append the anchor to the body
    document.body.appendChild(a);

    // Simulate a click on the anchor to trigger the download
    a.click();

    // Remove the anchor from the body
    document.body.removeChild(a);
  };
</script>

<div class="w-full flex flex-col justify-start">
  <Tile class="block">
    <p class="text-lg">Doctors consultation notes</p>
  </Tile>
  <TextArea
    hideLabel
    placeholder={`Record any notes not captured in the transcript here. You can then use "Generate" to autogenerate a full consultation summary.`}
    class="mt-2 block"
    bind:value
    on:change={setSummary}
    rows={30}
  />
  <ButtonSet class="flex justify-end mt-2">
    <Button icon={DiagramReference} class="block" kind="secondary" on:click={generate}>Generate</Button>
    <Button on:click={setSummary} class="block" icon={ArrowRight}>Save</Button>
  </ButtonSet>
  <div />
</div>
