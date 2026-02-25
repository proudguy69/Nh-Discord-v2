<template>
    <UPageSection>
        <UPageCard
        variant="subtle">
        <div class="flex items-center gap-1">
            <UAvatar src="https://cdn.discordapp.com/avatars/1267552151454875751/8a9584069302bc80962cc9e4dab99c84.webp" size="3xl"/>
            <div class="flex flex-col">
                <span class="font-bold">Paul</span>
                <span class="font-light">@orangegreencat</span>
            </div>
        </div>
        <ContentRenderer v-if="post" :value="post" />
        </UPageCard>
    </UPageSection>
</template>

<script setup lang="ts">

// varibles
const route = useRoute()
const blog = route.params.blog

console.log(route.fullPath)

const { data: post } = await useAsyncData(() => queryCollection('content').path('/blog/1').first())

useSeoMeta({
  title: post.value?.title,
  description: post.value?.description
})

</script>