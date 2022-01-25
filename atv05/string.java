public int findMinCutCost2(int[] m, int n) {
    if (m.length == 0) return 0;
    if (m.length == 1) return n;
       float half = n/2f;
       int bestIndex = 0;
       for (int i=1; i<m.length; i++) {
          if (Math.abs(half - m[bestIndex]) > Math.abs(half - m[i])) {
             bestIndex = i;
          }
       }
       int cl = 0, cr = 0;
       if (bestIndex > 0) {
          int[] ml = Arrays.copyOfRange(m, 0, bestIndex);
          int nl = m[bestIndex];
          cl = findMinCutCost2(ml, nl);
       }
       if (bestIndex < m.length - 1) {
          int[] mr = Arrays.copyOfRange(m, bestIndex + 1, m.length);
          int nr = n - m[bestIndex];
          for (int j=0; j<mr.length; j++) {
          mr[j] = mr[j] - m[bestIndex];
       }
       cr = findMinCutCost2(mr, nr);
    }
    return n + cl + cr;
 }