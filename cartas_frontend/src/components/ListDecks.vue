<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ListCards from './ListCards.vue';

interface Deck {
    id:number,
    name: string,
    card_count: number
}

const decks = ref([] as Deck[])
const new_deck_name = ref('')
const selected_deck = ref(1)

async function load_decks() {
    const list_decks = await axios.get<Deck[]>('http://127.0.0.1:8081/decks/')
    decks.value = list_decks.data
}

async function create_deck(){
  await axios.post('http://127.0.0.1:8081/decks/', {
    name: new_deck_name.value
  })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.error('Erro ao criar Deck:', error)
      })
}

function set_selected_deck(deck_id: number){
    selected_deck.value = deck_id
}

onMounted(async () => {
  await load_decks()  
})

</script>

<template>
  <main>
    <div class="decks">
      <div class="deck" v-for="deck in decks" :key="deck.id" @click="set_selected_deck(deck.id)">
        <p>{{ deck.name }} - {{ deck.card_count }}</p>
      </div>
    </div>

    <hr> <br>

    <label>Name: </label> <br>
    <input type="text" v-model="new_deck_name"> <br>
    <button class="c-button" @click="create_deck">Criar Deck</button>

    <hr>
    <ListCards :deck_id="selected_deck"></ListCards>
  </main>
</template>

<style scoped>

.decks {
  background-color: rgb(34, 34, 34);
  border: solid 1px rgb(3, 3, 3);
  height: 500px;
  width: 600px;
  margin: 5px;
  padding: 50px 20px 20px 20px;
  text-align: center;
}

.deck {
    background-color: rgb(54, 140, 151);
    height: 30px;
    border-radius: 2px;
    width: auto;
}

button {
  width: 316px;
  margin: 5px;
}

</style>
