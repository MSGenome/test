import gzip

class VCFParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        variants = []

        with gzip.open(self.file_path, 'rt') if self.file_path.endswith('.gz') else open(self.file_path, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue  # skip header lines
                fields = line.strip().split('\t')
                variant = {
                    'chrom': fields[0],
                    'pos': int(fields[1]),
                    'id': fields[2],
                    'ref': fields[3],
                    'alt': fields[4],
                    'qual': fields[5],
                    'filter': fields[6],
                    'info': fields[7],
                }
                variants.append(variant)

        return variants

# Example usage:
# parser = VCFParser('path/to/vcf_file.vcf')
# variants = parser.parse()
# print(variants)
