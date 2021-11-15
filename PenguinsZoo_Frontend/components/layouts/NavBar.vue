<template>
    <div
        class="
            bg-primary
            sticky
            top-0
            z-50
            w-full
            flex
            px-2
            py-1
            lg:px-8 lg:py-3
            justify-between
        "
    >
        <div class="lg:w-8 w-6">
            <NuxtLink to="/" @click.native="toggleCurr('home')"
                ><img src="../../static/logo.png"
            /></NuxtLink>
        </div>
        <div
            v-if="!this.currentId"
            class="
                flex
                text-xs
                lg:text-base
                text-white
                w-2/5
                lg:w-1/5
                justify-between
            "
        >
            <NuxtLink
                @click.native="toggleCurr('home')"
                class="
                    cursor-pointer
                    transition
                    transform
                    hover:underline
                    hover:text-hover
                    hover:font-extrabold
                    hover:-translate-y-1
                    hover:scale-110
                "
                :class="
                    $store.state.review.currentItem === 'home'
                        ? 'text-hover'
                        : ''
                "
                to="/"
            >
                <p class="divide-y">Home</p>
            </NuxtLink>
            <NuxtLink
                @click.native="toggleCurr('aboutus')"
                class="
                    cursor-pointer
                    hover:underline
                    transition
                    hover:text-hover
                    transform
                    hover:-translate-y-1 hover:scale-110
                "
                :class="
                    $store.state.review.currentItem === 'aboutus'
                        ? 'text-hover'
                        : ''
                "
                to="/about-us"
            >
                About us
            </NuxtLink>
            <NuxtLink
                class="
                    cursor-pointer
                    hover:underline
                    transition
                    transform
                    hover:text-hover hover:-translate-y-1 hover:scale-110
                "
                to="/login"
            >
                Login
            </NuxtLink>
        </div>
        <div
            v-else
            class="
                flex
                text-white text-sm
                lg:text-base
                w-4/5
                lg:w-1/3
                justify-between
            "
        >
            <NuxtLink
                @click.native="toggleCurr('home')"
                class="
                    cursor-pointer
                    transition
                    transform
                    hover:underline
                    hover:text-hover
                    hover:font-extrabold
                    hover:-translate-y-1
                    hover:scale-110
                "
                :class="
                    $store.state.review.currentItem === 'home'
                        ? 'text-hover'
                        : ''
                "
                to="/"
            >
                <p class="divide-y">Home</p>
            </NuxtLink>
            <NuxtLink
                @click.native="toggleCurr('review')"
                class="
                    cursor-pointer
                    hover:underline
                    transition
                    hover:text-hover
                    transform
                    hover:-translate-y-1 hover:scale-110
                "
                :class="
                    $store.state.review.currentItem === 'review'
                        ? 'text-hover'
                        : ''
                "
                to="review"
            >
                Review
            </NuxtLink>
            <NuxtLink
                @click.native="toggleCurr('completed')"
                class="
                    cursor-pointer
                    hover:underline
                    transition
                    hover:text-hover
                    transform
                    hover:-translate-y-1 hover:scale-110
                "
                :class="
                    $store.state.review.currentItem === 'completed'
                        ? 'text-hover'
                        : ''
                "
                to="completed"
            >
                Completed
            </NuxtLink>
            <NuxtLink
                @click.native="toggleCurr('aboutus')"
                class="
                    cursor-pointer
                    hover:underline
                    transition
                    hover:text-hover
                    transform
                    hover:-translate-y-1 hover:scale-110
                "
                :class="
                    $store.state.review.currentItem === 'aboutus'
                        ? 'text-hover'
                        : ''
                "
                to="/about-us"
            >
                About us
            </NuxtLink>
            <div
                class="
                    cursor-pointer
                    relative
                    hover:underline
                    transition
                    transform
                    hover:text-hover hover:-translate-y-1 hover:scale-110
                "
            >
                <p @click="showLogOut">
                    {{ currentUsername }}
                </p>
            </div>
            <div
                v-if="isShowLogOut"
                class="absolute mt-8 lg:mt-12 bg-primary px-5 py-2 right-0"
            >
                <NuxtLink
                    @click.native="logout"
                    class="cursor-pointer"
                    to="/login"
                >
                    Logout
                </NuxtLink>
            </div>
        </div>
    </div>
</template>

<script>
import NuxtLogo from '~/components/NuxtLogo'
import VueCookies from 'vue-cookies'
export default {
    name: 'navbar',
    components: { NuxtLogo },
    data() {
        return {
            currentId: 0,
            currentUsername: '',
            isShowLogOut: false,
        }
    },
    methods: {
        toggleCurr(header) {
            this.$store.state.review.currentItem = header
        },
        showLogOut() {
            this.isShowLogOut = !this.isShowLogOut
        },
        logout() {
            VueCookies.remove('id')
            VueCookies.remove('username')
        },
    },

    mounted() {
        this.currentId = VueCookies.get('id')
        this.currentUsername = VueCookies.get('username')
    },
}
</script>
