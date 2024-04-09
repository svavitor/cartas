<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Card {
  front: string,
  back: string,
  review_count: number,
  review_multiplier: number,
  last_review: any,
  next_review: any

}

const cards = ref([] as Card[])

async function loadCards() {
  const listCards = await axios.get<Card[]>('http://127.0.0.1:8081/cards/')
  cards.value = listCards.data
}

onMounted(async () => {
  await loadCards()  
})

</script>

<template>
  <div>
    <div v-for="(card, index) in cards" :key="index" class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <p>{{ card.front }}</p>
        </div>
        <div class="flip-card-back">
          <p>{{ card.back }}</p>
        </div>
      </div>
    </div> 
  </div>
  <main>

  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

 /* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
 .flip-card {
  border-radius: 12px;
  background-color: transparent;
  width: 300px;
  height: 200px;
  /* border: 1px solid #f1f1f1; */
  perspective: 1000px; /* Remove this if you don't want the 3D effect */
}

/* This container is needed to position the front and back side */
.flip-card-inner {
  border-radius: 12px;
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

/* Do an horizontal flip when you move the mouse over the flip box container */
.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

/* Position the front and back side */
.flip-card-front, .flip-card-back {
  position: absolute;
  border-radius: 12px;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
}

/* Style the front side (fallback if image is missing) */
.flip-card-front {
  background-color: #bbb;
  color: black;
}

/* Style the back side */
.flip-card-back {
  background-color: dodgerblue;
  color: white;
  transform: rotateY(180deg);
} 

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
