crud:
def update_produto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE produto SET produto = %s, descricao = %s, quantidade = %s, valorDeCompra = %s, valorDeVenda = %s, fornecedor = %s WHERE codproduto = %s"
    cursor.commit()
    cursor.close()
    conn.close()

TELA:
def update_produto(self):
            codigo_produto = self.CodigoEntry.get()
            produto = self.ProdutoEntry.get()
            descricao = self.DescricaoEntry.get()
            quantidade = self.QuantidadeEntry.get()
            valorDeCompra = self.ValorDeCompraEntry.get()
            valorDeVenda = self.ValorDeVendaEntry.get()
            fornecedor = self.FornecedorEntry.get()
            self.CodigoEntry.delete(0, tk.END)

            if codigo_produto and produto and descricao and quantidade and valorDeCompra and valorDeVenda and fornecedor:
                update_produto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor)
                self.ProdutoEntry.delete(0, tk.END)
                self.DescricaoEntry.delete(0, tk.END)
                self.QuantidadeEntry.delete(0, tk.END)
                self.ValorDeCompraEntry.delete(0, tk.END)
                self.ValorDeVendaEntry.delete(0, tk.END)
                self.FornecedorEntry.delete(0, tk.END)
                self.CodigoEntry.delete(0, tk.END)
                messagebox.showinfo("Success","Produto alterado com sucesso!")

            else:
                if codigo_produto == "" or produto == "" or descricao == "" or quantidade == "" or valorDeCompra == "" or valorDeVenda == "" or fornecedor == "":
                    messagebox.showinfo("Success","Todos os campos são obrigatórios!")
                else:
                    messagebox.showerror("Error","O Codigo de produto digitado não existe")
        
        AlterarButton = tk.Button(text = "ALTERAR",width=15,command=update_produto)
        AlterarButton.place(x=312,y=295)