(defun sumfib (a b c)
    (if (< b c) (+ (sumfib b (+ a b) c) (if (evenp b) b 0)) 0))

(print (sumfib 1 2 4000000))
