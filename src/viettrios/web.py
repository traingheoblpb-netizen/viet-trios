def tao_trang_chao():
    return """
    <html>
      <head>
        <title>Viet Trios</title>
        <style>
          body { font-family: Arial, sans-serif; background: #f5f5f5; padding: 40px; }
          .box { max-width: 700px; margin: auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
          h1 { color: #1c3c5c; }
          code { background: #eef2f7; padding: 4px 8px; border-radius: 6px; }
        </style>
      </head>
      <body>
        <div class="box">
          <h1>Viet Trios</h1>
          <p>He sinh thai lap trinh theo phong cach Python, viet bang tieng Viet khong dau.</p>
          <p>Trang nay la mot phan demo cho muc 4: web va api ket noi he thong.</p>
          <p>Lenh demo: <code>vtr chay examples/hello.vt</code></p>
        </div>
      </body>
    </html>
    """


def tao_trang_api():
    return {
        "ten": "Viet Trios",
        "trang_thai": "hoat_dong",
        "muc": "2_4"
    }
