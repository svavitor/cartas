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
const menu_screen = ref(true)
const review_screen = ref(false)

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
        console.error('Error creating new Deck:', error)
      })
}

function set_selected_deck(deck_id: number){
    selected_deck.value = deck_id
    review_screen.value = true
    menu_screen.value = false
}

function return_to_menu() {
    review_screen.value = false
    menu_screen.value = true
}

onMounted(async () => {
  await load_decks()  
})

</script>

<template>
  <main v-if="menu_screen">

    <div class="decks">
      <div class="deck" v-for="deck in decks" :key="deck.id" @click="set_selected_deck(deck.id)">
        <p>{{ deck.name }} - {{ deck.card_count }}</p>
      </div>
      <div v-if="decks.length < 1">No decks.</div>
    </div>


    <hr> <br>

    <label>Name: </label> <br>
    <input type="text" v-model="new_deck_name"> <br>
    <button class="c-button" @click="create_deck">Create Deck</button>

    <hr>
  </main>
  <ListCards v-if="review_screen" :deck_id="selected_deck"></ListCards>
  <button class="c-button" @click="return_to_menu">Deck Menu</button>
</template>

<style scoped>

.decks {
    background-color: rgb(245, 245, 245);
    border: solid 1px rgb(3, 3, 3);
    box-shadow: 4px 4px rgb(150, 150, 150);
    height: 500px;
    width: 600px;
    margin: 5px;
    padding: 50px 20px 20px 20px;
    text-align: center;
}

.deck {
    box-shadow: 4px 4px rgb(150, 150, 150);
    background-color: rgb(245, 245, 245);
    border: solid 1px rgb(3, 3, 3);
    border-radius: 0px;
    width: auto;
    height: 30px;
    margin: 6px;
    line-height: 1px;
}

.deck:hover {
    background-color: rgb(231, 231, 231);
    cursor: pointer;
}

button {
  width: 316px;
  margin: 5px;
}

</style>
