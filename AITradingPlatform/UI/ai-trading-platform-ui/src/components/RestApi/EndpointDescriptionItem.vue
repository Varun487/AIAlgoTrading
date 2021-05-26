<template>
  <div>

    <h2>{{ heading }}</h2>
    <hr />

    <ul v-for="api in apis" :key="api.code">
      <li :id="api.link" class="desc-item">
        <b class="api-type">{{ api.type }}</b> <Code :codetext="api.code" />
        <br />
        <br />

        {{ api.description }}
        <br />

        <h4 class="api-parameters">Parameters</h4>

        <table v-if="api.parameters">
          <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
          </tr>
          <tr v-for="parameter in api.parameters" :key="parameter.name">
            <td>{{ parameter.name }}</td>
            <td>{{ parameter.type }}</td>
            <td>{{ parameter.desc }}</td>
          </tr>
        </table>

        <h4 v-else  class="none" >None</h4>
        <br />

        <b class="api-correct-url">Sample request url: </b>
        <Code :codetext="api.req_url" />
        <br />
        <br />

        <b class="request-body">Request body </b>
		<JsonBlock v-if="api.req_body" :text="api.req_body" />
		<b v-else class="none" ><br /><br />None</b>
        <br />
        <br />

        <b class="correct-output">Correct Output </b>
        <JsonBlock v-if="api.correct_output" :text="api.correct_output" />
		<b v-else class="none" ><br /><br />None</b>
        <br />
        <br />

        <b class="failed-output">Failed Output </b>
        <JsonBlock v-if="api.failed_output" :text="api.failed_output" />
		<b v-else class="none" ><br /><br />None</b>
        <br />
        <br />
      </li>
    </ul>
  </div>
</template>

<script>
import Code from "../Common/Code.vue";
import JsonBlock from "../Common/JsonBlock.vue";

export default {
  name: "EndpointOverviewItem",
  components: {
    Code,
	JsonBlock,
  },
  props: {
    heading: String,
    apis: Array,
  },
};
</script>

<style scoped>
h2 {
  opacity: 0.9;
  padding-top: 20px;
}

a {
  color: #3291ff;
  opacity: 0.8;
  font-size: 13px;
}

ul {
  list-style-type: none;
}

hr {
  opacity: 0.2;
}

.desc-item {
  padding: 20px;
  padding-top: 100px;
}

table {
  width: 100%;
  padding-top: 20px;
  padding-bottom: 20px;
}

.api-type {
  color: lightgreen;
}

.api-correct-url {
  color: #fa8072;
}

.api-parameters {
  color: #1e90ff;
}

td {
  opacity: 0.8;
  padding-top: 10px;
  padding-right: 10px;
}

.none{
	opacity: 0.7;
}
</style>
