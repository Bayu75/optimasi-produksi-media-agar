
from flask import Flask, render_template
from scipy.optimize import linprog
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)


def hitung_optimasi():
    # Fungsi tujuan: memaksimalkan keuntungan
    # linprog melakukan minimisasi, sehingga koefisien dibuat negatif
    c = [-25000, -30000]

    # Kendala bahan baku
    # 2x + y <= 16 (nutrisi organik)
    # x + 3y <= 18 (hormon pertumbuhan)
    A_ub = [
        [2, 1],
        [1, 3]
    ]

    b_ub = [16, 18]

    # Jumlah produksi tidak boleh negatif
    bounds = [(0, None), (0, None)]

    hasil = linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        bounds=bounds,
        method="highs"
    )

    if not hasil.success:
        raise RuntimeError(
            f"Optimasi gagal: {hasil.message}"
        )

    # Mengambil hasil optimasi
    x = hasil.x[0]
    y = hasil.x[1]
    keuntungan = -hasil.fun

    # Menghitung penggunaan bahan baku
    nutrisi = 2 * x + y
    hormon = x + 3 * y

    return {
        "cokelat": x,
        "hijau": y,
        "keuntungan": keuntungan,
        "nutrisi": nutrisi,
        "sisa_nutrisi": 16 - nutrisi,
        "hormon": hormon,
        "sisa_hormon": 18 - hormon
    }


def buat_grafik(data):
    # Rentang nilai untuk menggambar garis kendala
    x = np.linspace(0, 10, 400)

    # Garis kendala:
    # 2x + y = 16  -> y = 16 - 2x
    # x + 3y = 18 -> y = (18 - x) / 3
    y_nutrisi = 16 - 2 * x
    y_hormon = (18 - x) / 3

    # Membatasi garis agar tidak tampil di bawah sumbu x
    y_nutrisi = np.where(y_nutrisi >= 0, y_nutrisi, np.nan)
    y_hormon = np.where(y_hormon >= 0, y_hormon, np.nan)

    fig, ax = plt.subplots(figsize=(8, 6))

    # Menggambar garis kendala
    ax.plot(
        x, y_nutrisi,
        label="2x + y = 16 (Nutrisi)",
        linewidth=2
    )
    ax.plot(
        x, y_hormon,
        label="x + 3y = 18 (Hormon)",
        linewidth=2
    )

    # Daerah layak: (0,0), (8,0), (6,4), (0,6)
    titik_x = [0, 8, 6, 0]
    titik_y = [0, 0, 4, 6]

    ax.fill(
        titik_x,
        titik_y,
        alpha=0.2,
        label="Daerah layak"
    )

    # Menandai solusi optimal
    ax.scatter(
        data["cokelat"],
        data["hijau"],
        color="red",
        s=100,
        zorder=5,
        label="Solusi optimal"
    )

    ax.annotate(
        f"({data['cokelat']:.0f}, {data['hijau']:.0f})",
        (data["cokelat"], data["hijau"]),
        xytext=(10, 10),
        textcoords="offset points"
    )

    ax.set_title("Optimasi Produksi Media Kultur Jaringan")
    ax.set_xlabel("Media Agar Cokelat (liter)")
    ax.set_ylabel("Media Agar Hijau (liter)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks(np.arange(0, 11, 1))
    ax.set_yticks(np.arange(0, 11, 1))
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()

    # Menyimpan grafik ke memori sebagai gambar PNG
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", dpi=120)
    buffer.seek(0)

    # Mengubah gambar menjadi Base64 untuk HTML
    grafik = base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")

    plt.close(fig)
    buffer.close()

    return grafik


@app.route("/")
def index():
    # Menghitung solusi optimal
    data = hitung_optimasi()

    # Membuat grafik berdasarkan hasil optimasi
    grafik = buat_grafik(data)

    # Mengirimkan hasil ke halaman HTML
    return render_template(
        "index.html",
        data=data,
        grafik=grafik
    )


if __name__ == "__main__":
    app.run(debug=True)
