class Complement
  def self.of_dna(strand='')
    return '' if strand == ''

    transcripted_strand = ''
    if strand.size == 1
      transcripted_strand << transcript(strand)
    else
      strand = strand.split ''
      strand.map { |nucleotide| transcripted_strand << transcript(nucleotide) }
    end

    transcripted_strand
  end

  def self.transcript(nucleotide)
    return 'C' if nucleotide == 'G'
    return 'G' if nucleotide == 'C'
    return 'A' if nucleotide == 'T'
    return 'U' if nucleotide == 'A'
  end
end
