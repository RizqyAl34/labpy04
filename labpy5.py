def atm_simulation():
    saldo = 1000000  # saldo awal
    print("Selamat datang di ATM!")
    print(f"Saldo Anda saat ini: Rp {saldo:,}")

    while True:
        print("\nMenu:")
        print("1. Tarik Uang")
        print("2. Keluar")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == '1':
            try:
                jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik: Rp "))
                if jumlah_tarik <= 0:
                    print("Jumlah yang ditarik harus lebih dari 0.")
                elif jumlah_tarik > saldo:
                    print("Saldo tidak mencukupi.")
                else:
                    saldo -= jumlah_tarik
                    print(f"Anda telah menarik: Rp {jumlah_tarik:,}")
                    print(f"Sisa saldo Anda: Rp {saldo:,}")
                    if saldo == 0:
                        print("Saldo Anda habis. Tidak bisa menarik lebih banyak.")
                        break
            except ValueError:
                print("Input tidak valid. Harap masukkan jumlah yang benar.")
        elif pilihan == '2':
            print("Terima kasih telah menggunakan ATM!")
            break
        else:
            print("Pilihan tidak valid. Harap pilih 1 atau 2.")

atm_simulation()
