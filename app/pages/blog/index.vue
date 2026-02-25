<template>
    <UPageSection>
        <UPageCard
        title="Blog posts",
        variant="subtle"
        >
        <UBlogPosts orientation="vertical" :posts="posts"/>
        </UPageCard>
    </UPageSection>
</template>

<script setup lang="ts">
import type { BlogPostProps } from '@nuxt/ui'

const posts = ref<BlogPostProps[]>([
    {
        title: 'Community Update #1',
        description: 'The first of many community updates!',
        date: '02/24/2026',
        badge: 'Community Update',
        orientation: 'vertical',
        to: '/blog/1',
        authors: [
            {
                name: 'Paul',
                description: '@orangegreencat',
                avatar: {src: 'https://cdn.discordapp.com/avatars/1267552151454875751/8a9584069302bc80962cc9e4dab99c84.webp'}
            }
        ]
  },
])
    
</script>