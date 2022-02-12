{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Wired Graph.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Alan-Fu/pcc_2e/blob/master/CS131-h4-2-Alan.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "2Atudw25C3bL",
        "outputId": "7db1eb05-db47-438a-ca7b-15607db39480"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "# CS131-hwD-p2-Alan\n",
        "\n",
        "import matplotlib.pyplot as plt\n",
        "x = list(range(0,21,1))\n",
        "y = [0.0]*len(x)\n",
        "slope = 2.\n",
        "#MODIFY y here\n",
        "y[2] = 2.\n",
        "y[3] = 2.\n",
        "\n",
        "for i in range(4):\n",
        "  y[6+i] = slope*i\n",
        "\n",
        "for i in reversed(range(4)):\n",
        "  y[10+i] = 6-slope*i\n",
        "\n",
        "for i in range(len(x[14:])):\n",
        "  y[14+i]=i**0.5\n",
        "\n",
        "plt.plot(x,y,'b-o') #Color, change 'b' for blue to 'r' for red\n",
        "plt.show()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        ""
      ],
      "metadata": {
        "id": "VAj1tjsVHiyD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "3HHL_GM5C_YQ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}