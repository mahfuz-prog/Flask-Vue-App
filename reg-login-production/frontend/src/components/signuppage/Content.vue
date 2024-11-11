<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useNotification } from "@kyvg/vue3-notification"

const notification = useNotification()
const router = useRouter()

const submitValues = ref({
  name: null,
  email: null,
  password: null,
  createTime: null
})
const submitErrors = ref({})
const isSubmitted = ref(false)
const submitBtn = ref('Sign Up')
const verifyErrors = ref()
const verifyValue = ref(null)
const hmac = ref()
const submitVerifyBtn = ref('Verify')
const resendBtn = ref(false)
const resendVeifyBtn = ref('Resend Code')


// handle user info input and validation
async function submitForm() {
  submitErrors.value = {}

  // name validation
  if (!validateName(submitValues.value.name)) {
    submitErrors.value.name = 'Only 3 - 25 characters allowed "a-Z, 0-9, _, -, space"'
  }

  // email validation
  if (!validateEmail(submitValues.value.email)) {
    submitErrors.value.email = 'Please enter a valid email address.'
  }

  // password validation
  if (!validatePassword(submitValues.value.password)) {
    submitErrors.value.password = '8 characters lowercase, uppercase, digit'
  }

  // check username and email in database
  // if those exist in database give an validation error
  // this request also return a hash of user information, otp & time if there is no user
  if (Object.keys(submitErrors.value).length === 0) {
    submitBtn.value = 'Submiting'

    submitValues.value.createTime = new Date()
    const data = await (await axios.post('sign-up/', submitValues.value)).data

    // variable for backend error
    const nameStatus = data.nameStatus
    const emailStatus = data.emailStatus
    const emailSentStatus = data.emailSentStatus

    // username error from backend
    if (nameStatus) {
      submitErrors.value.name = nameStatus
    }

    // email error from backend
    if (emailStatus) {
      submitErrors.value.email = emailStatus
    }

    // if backend fail to send otp in email this error will trigger
    if (emailSentStatus) {
      notification.notify({ title: "Otp Send Failed", text: "Please re submit this form again!" })
    }

    // finally complete validation
    // store the hmac which will send to verify the otp again in backend
    if (!nameStatus && !emailStatus && !emailSentStatus) {
      hmac.value = data
      isSubmitted.value = true
      notification.notify({ title: "Please verify OTP", text: "A 6 digit code has been send in your email." })

      // we will only allow users to request for a new otp after 2 minutes
      // resendBtn show the button that trigger resendCode()
      setTimeout(() => { resendBtn.value = true }, 120000)
    } else {
      submitBtn.value = 'Sign Up'
    }
  }
}


// allow users to input username only using those character a-Z, 0-9, -, _, Spaces
// minimum 3 maximum 25
function validateName(name) {
  const re = /^[a-zA-Z0-9_\s-]{3,25}$/
  return re.test(name)
}

// email validation
function validateEmail(email) {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  return re.test(String(email).toLowerCase())
}

// password validation
// must one lowercase, one uppercase, one digit, minimum 8 digit and mximum 20
function validatePassword(password) {
  const re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$/
  return re.test(password)
}


// use input otp from email
// send the otp, hash, and user info to verifi and create user in backend
async function verifyForm() {
  verifyErrors.value = ""

  if (!validateOtp(verifyValue.value)) {
    verifyErrors.value = 'Only 6 digit code'
  }

  if (verifyErrors.value.length === 0) {
    const payload = { info: submitValues.value, hmac: hmac.value, otp: verifyValue.value }

    try {
      submitVerifyBtn.value = 'Submiting'
      const data = await (await axios.post('verify/', payload)).data
      if (data === 'verified') {
        router.push('/log-in')
        notification.notify({ title: "Account Created 🎉", text: "Now you can log in." })
      }
    } catch (err) {
      // server side error
      verifyErrors.value = "Timeout or Wrong OTP"
      submitVerifyBtn.value = 'Verify'
    }
  }
}

// allows only input 6 digit otp
function validateOtp(otp) {
  const re = /^\d{6}$/
  return re.test(otp)
}


// this function resubmit the users information to update time and otp
async function resendCode() {
  resendVeifyBtn.value = 'Sending'
  await submitForm()
  resendBtn.value = false
  verifyValue.value = null
  resendVeifyBtn.value = 'Resend Code'
}
</script>
<template>
  <div class="form">
    <!-- user data input form -->
    <form @submit.prevent="submitForm" v-if="!isSubmitted" method="POST">
      <h4>Create Account</h4>
      <input type="text" id="name" v-model.trim="submitValues.name" placeholder="Your Name" required/>
      <span v-if="submitErrors.name">● {{ submitErrors.name }}</span>
      <input type="email" id="email" v-model.trim="submitValues.email" placeholder="Your Email" required/>
      <span v-if="submitErrors.email">● {{ submitErrors.email }}</span>
      <input type="password" id="password" v-model.trim="submitValues.password" placeholder="Password" required/>
      <span v-if="submitErrors.password">● {{ submitErrors.password }}</span>
      <button type="submit" :class="{ deactive : submitBtn==='Submiting' }">{{ submitBtn }}</button>
    </form>
    <!-- otp verification form -->
    <form @submit.prevent="verifyForm" v-if="isSubmitted" method="POST">
      <h4>Please Put the OTP from your email</h4>
      <input type="text" id="verify" v-model.trim="verifyValue" placeholder="6 Digit code" required/>
      <span v-if="verifyErrors">● {{ verifyErrors }}</span>
      <button type="submit" :class="{ deactive : submitVerifyBtn==='Submiting' }">{{ submitVerifyBtn }}</button>
    </form>
    <button class="resend-btn" v-if="resendBtn" @click="resendCode" :class="{ deactive : resendVeifyBtn === 'Sending' }">
      {{ resendVeifyBtn }}
    </button>
  </div>
</template>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 15px;
}

.form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-radius: 5px;
  padding: 30px;
  width: 350px;
  background-color: var(--secondary-black);
}

input {
  color: #fff;
  border: 0;
  border-radius: 3px;
  width: 100%;
  padding: 10px 15px 10px 15px;
  background-color: var(--tertiary-black);
}

input:focus-visible {
  outline: none;
  color: #fff;
}

button,
input[type="submit"] {
  border: 0;
  background-color: var(--accent);
  border-radius: 25px;
  padding: 9px;
  color: #fff;
  cursor: pointer;
}

.resend-btn {
  margin-top: 15px;
  background-color: var(--tertiary-black);
}

.deactive {
  animation: btn-bg 1s infinite;
}

span {
  color: red;
  padding-left: 5px;
  margin-top: -10px;
  font-size: 12px;
  font-weight: 400;
}

h4 {
  color: #fff;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
}

@keyframes btn-bg {
  0% {
    background-color: var(--tertiary-black);
  }
  50% {
    background-color: rgb(145 145 145 / 64%);
  }
  100% {
    background-color: var(--tertiary-black);
  }
}
</style>
