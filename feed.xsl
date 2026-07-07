<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title><xsl:value-of select="/rss/channel/title"/> — RSS Feed</title>
        <style>
          :root{--ink:#06483f;--muted:#4a6b64;--accent:#00695c;--bg:#ffffff;--rule:#e7e0d6}
          body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6}
          .container{max-width:44rem;margin:0 auto;padding:1.5rem 1.25rem 4rem}
          a{color:var(--accent);text-decoration:none}
          a:hover{text-decoration:underline}
          .banner{background:#e3f3ec;border:1px solid var(--accent);border-radius:8px;padding:1rem 1.25rem;margin:1rem 0 2rem;font-size:.95rem}
          h1{font-size:1.8rem;margin:.25rem 0}
          h2{font-size:1.2rem;margin-top:2rem}
          .desc{color:var(--muted)}
          .item{padding:1rem 0;border-bottom:1px solid var(--rule)}
          .item .title{font-size:1.15rem;font-weight:600}
          .item .date{color:var(--muted);font-size:.82rem;margin:.15rem 0}
          .item p{margin:.4rem 0 0;color:var(--muted)}
        </style>
      </head>
      <body>
        <div class="container">
          <div class="banner">
            <strong>📡 This is an RSS feed.</strong> It updates automatically when new posts go live. Paste this page's web address into an RSS reader app (Feedly, Inoreader, NetNewsWire, and many others) to subscribe and never miss a post.
          </div>
          <h1><xsl:value-of select="/rss/channel/title"/></h1>
          <p class="desc"><xsl:value-of select="/rss/channel/description"/></p>
          <p><a href="{/rss/channel/link}">&#8592; Back to the website</a></p>
          <h2>Latest posts</h2>
          <xsl:for-each select="/rss/channel/item">
            <div class="item">
              <a class="title" href="{link}"><xsl:value-of select="title"/></a>
              <div class="date"><xsl:value-of select="pubDate"/></div>
              <p><xsl:value-of select="description"/></p>
            </div>
          </xsl:for-each>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
