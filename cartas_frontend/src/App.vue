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
      <ul>
        <li v-for="(card, index) in cards" :key="index">
        
          {{ card.front }} <br>
          {{ card.back }}
        
        </li>
      </ul>
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
