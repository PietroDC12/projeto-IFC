<template>
  <div class="container">
    <div id="app">
      <h1>Campanhas Solidárias</h1>
      <p v-for="campanha in campanhas" :key="campanha.campanha_id">
        Nome da Campanha: {{ campanha.titulo_campanha }}
      </p>
      <p v-for="campanha in campanhas" :key="campanha.campanha_id">
        Data início: {{ campanha.dt_inicio_campanha }}
      </p>
      <p v-for="campanha in campanhas" :key="campanha.campanha_id">
        Data fim: {{ campanha.dt_fim_campanha }}
      </p>
      <p v-for="campanha in campanhas" :key="campanha.campanha_id">
        Endereço campanha: <br />
        <b>Rua </b> {{ campanha.rua_campanha }}<br />
        <b>Número</b> {{ campanha.numero_endereco_campanha }} <br />
        <b>Bairro</b> {{ campanha.bairro_campanha }} <br />
        <b>Cidade</b> {{ campanha.cidade_campanha }} <br />
      </p>
      <p v-for="campanha in campanhas" :key="campanha.campanha_id">
        Link: {{ campanha.link_campanha }}
      </p>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "CampanhaListUni",
  data() {
    return {
      newCampanha: "",
      campanhas: [],
    };
  },
  mounted() {
    this.getCampanhaId();
  },
  methods: {
    getCampanhaId() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: `/api/campanhas/get/${this.$route.params.id}/`
        })
        .then(res => {
          this.campanhas = res.data
          console.log(res)
        });
    },
  },
};
</script>

<style>
</style>