Module Bernoulli30
    Function Binomial(n As Integer, k As Integer) As Long
        If k = 0 Or k = n Then
            Return 1
        End If
        Return Binomial(n-1, k-1) + Binomial(n-1, k)
    End Function
    
    Function Bernoulli(n As Integer) As Double
        If n = 0 Then
            Return 1.0
        End If
        If n = 1 Then
            Return -0.5
        End If
        If n Mod 2 = 1 And n > 1 Then
            Return 0.0
        End If
        
        Dim sum As Double = 0.0
        For k As Integer = 0 To n-1
            sum += Binomial(n, k) * Bernoulli(k) / (n - k + 1)
        Next
        Return -sum
    End Function
    
    Sub Main()
        Console.WriteLine(Bernoulli(30))
    End Sub
End Module