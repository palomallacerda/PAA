
function TcpPrim(I, α, o, c, d)
   t_restantes <-- I.terminais
   fila <-- Ø
   custos[v] ← ∞ ∀v  I
   MST[v] ← False  ∀v  I 
   Pais[v] ← -1 ∀v  I
   graus ← 0 ∀v  I
   E ←  0
   R ←  0
   fila.add({o,0})
   while fila 6 = Ø do
       if c do
           update(graus, E,R)
            E ←  choose_Next(Fila, infinito, I.maxE,I.maxR, E,R, pais, graus)
       end if
       else if
           A ←  elemento aleatório entre  *|fila| primeiros elementos da fila
	end else
    v <-- fila.remove(A)
    MST[v] <-- True if v E I.terminais então
        terminais_restantes.remove(v)
        end if 
        For todo u conectao a v do
            d <-- custo({u,v})
            if MST[u] = False && custo[u]> d 
                fila.add(u,d)
                pais[u] <-- v
                custo[u] <-- d
            end if
        end For
    end while
    g < -- construir_graph(pais,custo)
    g.reduzir()
    atulizar(graus,E,R)
    if( [d &(E > I.maxE or R > I.maxR)] or terminais_restantes 6= Ø) 
        g <-- Ø
    end if
    return g
end function