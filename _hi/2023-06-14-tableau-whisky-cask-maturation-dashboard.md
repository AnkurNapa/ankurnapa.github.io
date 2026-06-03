---
layout: post
lang: hi
title: "Tableau में कास्क मैच्योरेशन और एंजल्स-शेयर डैशबोर्ड"
image: /assets/og/tableau-whisky-cask-maturation-dashboard.png
description: "उम्र, सामर्थ्य और एंजल्स-शेयर वाष्पीकरण हानि को ट्रैक करने वाला Tableau कास्क मैच्योरेशन डैशबोर्ड बनाएं, जिसमें अनुमानित तैयार-तिथियां और AI-संचालित निगरानी हो।"
date: 2023-06-14
updated: 2023-06-14
permalink: /hi/2023/tableau-whisky-cask-maturation-dashboard/
tags: [distilling-maturation, tableau, whiskey]
faq:
  - q: "मैं Tableau में एंजल्स शेयर को कैसे मॉडल करूं?"
    a: "एक टेबल कैलकुलेशन का उपयोग करें जो प्रत्येक कास्क की मैच्योरेशन समयरेखा में एक वार्षिक हानि दर (लगभग 2% प्रति वर्ष) को चक्रवृद्धि करता है, आदर्श रूप से एक सपाट अनुमान के बजाय आपके अपने तौल रिकॉर्ड के विरुद्ध अंशांकित।"
  - q: "क्या Tableau यह पूर्वानुमान कर सकता है कि कोई कास्क कब तैयार होगा?"
    a: "हां, एक कैलकुलेटेड फ़ील्ड के माध्यम से जो सामर्थ्य और आयतन को आपकी लक्ष्य उम्र तक आगे प्रक्षेपित करता है, लेकिन तिथि को एक योजना अनुमान मानें, वादा नहीं, क्योंकि प्रति-कास्क भिन्नता बड़ी होती है।"
  - q: "क्या Tableau मास्टर ब्लेंडर की जगह ले लेता है?"
    a: "नहीं। Tableau स्टॉक की निगरानी करता है और सूंघने योग्य कास्क को चिह्नित करता है; बोतलबंद करने का निर्णय अब भी ब्लेंडिंग टीम के संवेदी मूल्यांकन पर टिका रहता है।"
---

**संक्षिप्त उत्तर: Tableau बिखरे हुए कास्क रिकॉर्ड को एक जीवंत मैच्योरेशन व्यू में बदल देता है जो दिखाता है कि आपके पास क्या है, यह कितनी तेज़ी से वाष्पित हो रहा है, और लगभग कब तैयार है।** कठिन हिस्सा चार्ट नहीं हैं; यह है साफ़ डेटा रखना और यह स्वीकार करना कि व्हिस्की एक ऐसी समयावधि पर चलती है जिसे कोई डैशबोर्ड तेज़ नहीं कर सकता।

<figure style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 1000 380" width="100%" style="max-width:1000px;height:auto" role="img" aria-label="Tableau में कास्क मैच्योरेशन और एंजल्स-शेयर डैशबोर्ड के लिए सामान्य डैशबोर्ड लेआउट"><rect x="0" y="0" width="1000" height="380" fill="#fdfbf7"/><text x="500" y="26" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="#b45309">डैशबोर्ड लेआउट</text><text x="500" y="52" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#1c1a17">Tableau में कास्क मैच्योरेशन और एंजल्स-शेयर डैशबोर्ड</text><rect x="40" y="64" width="920" height="30" rx="6" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="52" y="84" font-family="sans-serif" font-size="12.5" fill="#6b6258">फ़िल्टर:</text><rect x="120" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="250" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="380" y="71" width="100" height="16" rx="8" fill="#fdfbf7" stroke="#b45309"/><rect x="40" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="58" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 1</text><rect x="58" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="355" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="373" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 2</text><rect x="373" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="670" y="108" width="290" height="74" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="688" y="134" font-family="sans-serif" font-size="12" fill="#6b6258">KPI 3</text><rect x="688" y="144" width="120" height="20" rx="3" fill="#b45309"/><rect x="40" y="198" width="575" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="56" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">ट्रेंड</text><rect x="120" y="268" width="46" height="70" fill="#b45309"/><rect x="200" y="243" width="46" height="95" fill="#b45309"/><rect x="280" y="278" width="46" height="60" fill="#b45309"/><rect x="360" y="228" width="46" height="110" fill="#b45309"/><rect x="440" y="253" width="46" height="85" fill="#b45309"/><rect x="520" y="218" width="46" height="120" fill="#b45309"/><rect x="640" y="198" width="320" height="150" rx="8" fill="#ffffff" stroke="#e0d8cc" stroke-width="1.5"/><text x="656" y="220" font-family="sans-serif" font-size="12.5" fill="#6b6258">विभाजन</text><rect x="656" y="238" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="238" width="60" height="10" rx="3" fill="#b45309"/><rect x="656" y="264" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="264" width="50" height="10" rx="3" fill="#b45309"/><rect x="656" y="290" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="290" width="40" height="10" rx="3" fill="#b45309"/><rect x="656" y="316" width="200" height="10" rx="3" fill="#f7ece0"/><rect x="876" y="316" width="30" height="10" rx="3" fill="#b45309"/></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">इस डैशबोर्ड का एक सामान्य लेआउट: ऊपर मुख्य मेट्रिक, नीचे एक ट्रेंड और एक विभाजन, और इसे काटने के लिए फ़िल्टर।</figcaption>
</figure>

## पहले माप, फिर विज़ुअलाइज़ेशन
Tableau खोलने से पहले तय करें कि डेटा की हर पंक्ति क्या दर्शाती है। स्वाभाविक ग्रेन एक कास्क-दर-तिथि अवलोकन है: कास्क ID, फ़िल तिथि, कास्क प्रकार (एक्स-बर्बन, एक्स-शेरी, वर्जिन ओक), शुद्ध अल्कोहल के मूल लीटर, वर्तमान सामर्थ्य, और प्रत्येक तौल या डिप की तिथि। अधिकांश डिस्टिलरी हर कास्क को हर महीने नहीं तौलतीं, इसलिए आपका डेटा स्रोत विरल और असमान होगा। इसे ईमानदारी से मॉडल करें। यदि आपका वेयरहाउस सिस्टम समर्थन करता है तो इसे लाइव कनेक्शन के रूप में लाएं, या कुछ भी बनाने से पहले इसे Tableau Prep में एक साफ़-सुथरे एक्सट्रैक्ट (.hyper) में आकार दें।

पहले ग्रेन परिभाषित करने का अनुशासन ही वह चीज़ है जो एक असली रैकहाउस के संपर्क में टिकने वाले डैशबोर्ड को एक सुंदर डेमो से अलग करती है। इसे ग़लत करें और नीचे का हर कैलकुलेटेड फ़ील्ड वही त्रुटि विरासत में पाता है।

## संचयी हानि और अनुमानित तैयार-तिथियां
एंजल्स शेयर — वाष्पीकरण में खोई स्पिरिट, प्रति वर्ष आयतन का लगभग 2% पर अत्यधिक परिवर्तनशील — मुख्य मेट्रिक है। इसे एक टेबल कैलकुलेशन से मॉडल करें जो प्रत्येक कास्क के जीवन में वार्षिक हानि को चक्रवृद्धि करता है, कास्क ID द्वारा विभाजित और तिथि के अनुसार क्रमित। एक LOD एक्सप्रेशन जैसे `{ FIXED [Cask ID] : MIN([Fill Date]) }` आपको प्रति कास्क एक स्थिर मैच्योरेशन-उम्र फ़ील्ड देता है, चाहे उपयोगकर्ता जो भी फ़िल्टर लगाए।

लक्ष्य उम्र के लिए एक पैरामीटर डालें ताकि उपयोगकर्ता पूछ सके: कौन से कास्क अगली तिमाही में बारह वर्ष तक पहुंचते हैं? एक व्हाट-इफ़ एक्शन आपको मान ली गई हानि दर को बदलने और अनुमानित आयतन व सामर्थ्य की प्रतिक्रिया देखने देता है। Tableau Pulse फिर प्रकाशित वर्कबुक के ऊपर बैठ सकता है और टीम को बिना डैशबोर्ड खोले एक सरल-भाषा सारांश भेज सकता है — "वेयरहाउस 3 ने इस तिमाही पिछली तिमाही की तुलना में 0.4% अधिक खोया"।

## यह कहां टूटता है
यह डैशबोर्ड उतना ही अच्छा है जितनी आपके मापों की लय है। यदि कास्क साल में एक बार तौले जाते हैं, तो आपकी संचयी-हानि वक्र दो बिंदुओं के बीच एक प्रक्षेप है, और अनुमानित तैयार-तिथि वर्षों की अनिश्चितता ढोती है। Tableau में अंतर्निहित पूर्वानुमान एक्सपोनेंशियल स्मूदिंग का उपयोग करता है, जो एक सहज ट्रेंड के लिए ठीक है लेकिन लकड़ी, फ़िल सामर्थ्य और वेयरहाउस की स्थिति से संचालित कास्क-दर-कास्क भिन्नता को नहीं पकड़ सकता। इसके लिए आपको या तो समृद्ध डेटा चाहिए या TabPy के माध्यम से एक बाहरी मॉडल — मॉडलिंग पक्ष के लिए [व्हिस्की के एंजल्स शेयर का पूर्वानुमान]({{ '/hi/2024/forecasting-whiskey-angels-share/' | relative_url }}) देखें।

गहरी सीमा भौतिकी है। मैच्योरेशन वर्षों में फ़ीडबैक देती है, इसलिए डैशबोर्ड धैर्य को पुरस्कृत करता है, गति को नहीं। यह आपको आपके स्टॉक की स्थिति बताता है; यह स्पिरिट को ज़रा भी जल्दी तैयार नहीं करता।

<figure data-d2="1" style="margin:1.6rem 0;text-align:center">
<svg viewBox="0 0 720 300" width="100%" style="max-width:720px;height:auto" role="img" aria-label="मैच्योरेशन को क्या चलाता है, और यह आगे क्या बदलता है।"><rect x="0" y="0" width="720" height="300" fill="#fdfbf7"/><text x="360.0" y="24" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" letter-spacing="1.5" fill="#b45309">इसे क्या चलाता है</text><text x="360.0" y="47" text-anchor="middle" font-family="sans-serif" font-size="15.5" font-weight="700" fill="#1c1a17">Tableau में कास्क मैच्योरेशन और एंजल्स-शेयर डैशबोर्ड</text><rect x="50" y="90" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="118" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">इनपुट 1</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="112" x2="285" y2="150"/></g><rect x="50" y="150" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="178" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">इनपुट 2</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="172" x2="285" y2="150"/></g><rect x="50" y="210" width="130" height="44" rx="8" fill="#f7ece0" stroke="#b45309" stroke-width="1.5"/><text x="115" y="238" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#6b6258">इनपुट 3</text><g fill="#b45309" stroke="#b45309" stroke-width="2"><line x1="180" y1="232" x2="285" y2="150"/></g><rect x="290" y="116" width="140" height="68" rx="10" fill="#b45309"/><text x="360" y="156" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#ffffff">मैच्योरेशन</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="142"/><polygon points="535,135 547,142 535,149" stroke="none"/></g><rect x="550" y="120" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">गुणवत्ता</text><g fill="#5b7a1f" stroke="#5b7a1f" stroke-width="2"><line x1="430" y1="150" x2="535" y2="202"/><polygon points="535,195 547,202 535,209" stroke="none"/></g><rect x="550" y="180" width="130" height="44" rx="8" fill="#f7ece0" stroke="#5b7a1f" stroke-width="1.5"/><text x="615" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1c1a17">लागत / जोखिम</text></svg>
<figcaption style="font-size:.85rem;color:#6b6258;margin-top:.4rem">मैच्योरेशन को क्या चलाता है, और यह आगे क्या बदलता है।</figcaption>
</figure>

## निष्कर्ष
एक Tableau कास्क मैच्योरेशन डैशबोर्ड आपकी पूरी परिपक्व हो रही इन्वेंट्री को एक साथ देखने, वाष्पीकरण को ईमानदारी से ट्रैक करने, और यथार्थवादी तैयार-तिथियों के आसपास बोतलबंदी की योजना बनाने का सबसे सस्ता तरीका है। इसके प्रक्षेपणों को योजना सहायक मानें और मास्टर ब्लेंडर की नाक को अंतिम उपकरण बनाए रखें। अच्छी तरह बनाया जाए, तो यह हज़ारों कास्क में से उन गिने-चुने कास्क को उजागर करके अपनी कीमत वसूल करता है जिन्हें इस महीने ध्यान की ज़रूरत है।

*[Distilling & Maturation]({{ '/hi/tracks/distilling-maturation/' | relative_url }}) ट्रैक का हिस्सा।* संबंधित: [व्हिस्की के एंजल्स शेयर का पूर्वानुमान]({{ '/hi/2024/forecasting-whiskey-angels-share/' | relative_url }})।

## अक्सर पूछे जाने वाले प्रश्न

**मैं Tableau में एंजल्स शेयर को कैसे मॉडल करूं?**
एक टेबल कैलकुलेशन का उपयोग करें जो प्रत्येक कास्क की मैच्योरेशन समयरेखा में एक वार्षिक हानि दर (लगभग 2% प्रति वर्ष) को चक्रवृद्धि करता है, आदर्श रूप से एक सपाट अनुमान के बजाय आपके अपने तौल रिकॉर्ड के विरुद्ध अंशांकित।

**क्या Tableau यह पूर्वानुमान कर सकता है कि कोई कास्क कब तैयार होगा?**
हां, एक कैलकुलेटेड फ़ील्ड के माध्यम से जो सामर्थ्य और आयतन को आपकी लक्ष्य उम्र तक आगे प्रक्षेपित करता है, लेकिन तिथि को एक योजना अनुमान मानें, वादा नहीं, क्योंकि प्रति-कास्क भिन्नता बड़ी होती है।

**क्या Tableau मास्टर ब्लेंडर की जगह ले लेता है?**
नहीं। Tableau स्टॉक की निगरानी करता है और सूंघने योग्य कास्क को चिह्नित करता है; बोतलबंद करने का निर्णय अब भी ब्लेंडिंग टीम के संवेदी मूल्यांकन पर टिका रहता है।
