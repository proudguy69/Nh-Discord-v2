<template>
  <div v-if="userInfo.username">
    <span>{{ userInfo.username }}</span>
    <img :src="userInfo.avatar" class="h-[64px]">
  </div>
  <UApp>
    <UButton :to="authUri" label="discord auth"/>
    <NuxtPage />
  </UApp>
</template>

<script setup lang="ts">
// interfaces
interface UserInfo {
    username:string|undefined
    avatar:string|undefined
}

// varibles
const authUri = {
  dev: 'https://discord.com/oauth2/authorize?client_id=1304965391507914782&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A3001%2Fauthorize&scope=identify+guilds+guilds.join+email'
}.dev

const appUri = {
  dev: 'http://localhost:8000'
}.dev

// refs
const userInfo = ref<UserInfo>({
  username:undefined,
  avatar:undefined
})

// provides
provide('appUri', appUri)
provide('userInfo', userInfo)

// methods
onMounted(async () => {
  const web_token = localStorage.getItem('web_token')
  if (web_token) {
    userInfo.value.username = localStorage.getItem('username')!
    userInfo.value.avatar = localStorage.getItem('avatar')!
  }
})

</script>