---
layout: page
title: "Contact & Feedback"
permalink: /contact/
description: "Send a suggestion, report an issue, or message Ankur Napa directly about beer, wine, whiskey, and AI."
---

Got a suggestion, spotted something wrong, or just want to ask a question about beer, wine, whiskey, and AI? Use the form below and it lands straight in my inbox — I read every message.

<form action="https://formsubmit.co/REPLACE_WITH_YOUR_FORMSUBMIT_CODE" method="POST" class="contact-form">
  <input type="hidden" name="_subject" value="New message from Beer, Wine, Whiskey & AI">
  <input type="hidden" name="_template" value="table">
  <input type="hidden" name="_captcha" value="true">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">

  <label for="cf-name">Name</label>
  <input id="cf-name" type="text" name="name" required>

  <label for="cf-email">Your email</label>
  <input id="cf-email" type="email" name="email" required>

  <label for="cf-type">What's this about?</label>
  <select id="cf-type" name="type">
    <option>Suggestion</option>
    <option>Improvement idea</option>
    <option>Question</option>
    <option>Spotted an error</option>
    <option>Just saying hello</option>
  </select>

  <label for="cf-message">Message</label>
  <textarea id="cf-message" name="message" rows="6" required></textarea>

  <button type="submit" class="cta">Send message</button>
</form>

<p class="contact-note">Your email is only used to reply. No newsletter, no sharing.</p>
